% Open all files as a cell
numfiles = 12;
images = cell(1, numfiles);

for i = 1:9
    filename = sprintf('0%d.jpg', i);
    images{i} = imread(filename);
end

for i = 10:numfiles
    filename = sprintf('%d.jpg', i);
    images{i} = imread(filename);
end

%rgbImage = imread('01.jpg', 'jpg');

%% Create feature vector
% 1,2,3: Mean color content (RGB)
% 4,5,6: Mean color in center (RGB)
% 7: Luminance distribution in center
% 8,9: Angle and length for longest line
% 10,11: Angle and length for the second longest line
% 12,13: Angle and length for the third longest line
% 14,15: Angle and length for the fourth longest line
F = zeros(15,12);
%% Mean/average color content
meanVector = zeros(3,12);
% For every image, take the mean of the three channels
for i = 1:12
    meanVector(1,i) = mean2(images{i}(:,:,1));
    meanVector(2,i) = mean2(images{i}(:,:,2));
    meanVector(3,i) = mean2(images{i}(:,:,3));
end
% Add to feature vector
F(1:3, :) = meanVector;
%% Test of mean color value
testImage = ones(100,100,3);

testImage(:,:,1) = meanVector(1,1) / 255;
testImage(:,:,2) = meanVector(2,1) / 255;
testImage(:,:,3) = meanVector(3,1) / 255;

imshow(testImage)

%% Colour distribution around central point
% Find center points in all images
centers = zeros(2,12);
for i = 1:12
    [centers(1,i), centers(2,i)] = findCenterPoint(images{i});
end

%[meanR, meanG, meanB] = getPointColorDist(images{1}, centers(1,1), centers(2,1), 100);

% Get the mean value for all channels for all images
d = 100;
meanCenterVector = zeros(3,12);
for i = 1:12
    %figure
    %subplot(1,2,1)
    [meanCenterVector(1,i), meanCenterVector(2,i), meanCenterVector(3,i)] = getPointColorDist(images{i}, centers(1,i), centers(2,i), d);
    testImage = ones(d*2, d*2,3);

    testImage(:,:,1) = meanCenterVector(1,i) / 255;
    testImage(:,:,2) = meanCenterVector(2,i) / 255;
    testImage(:,:,3) = meanCenterVector(3,i) / 255;
    %subplot(1,2,2)
    %imshow(testImage)
    
end
% Add to featur vector
F(4:6, :) = meanCenterVector;

%% Luminance distribution
lumVector = zeros(1,12);

for i = 1:12
    lumVector(i) = lumPointDist(images{i}, centers(1,i), centers(2,i), 100);
end

% Add to feature vector
F(7, :) = lumVector(:);

%% Använd binärfilerna och gå igenom dem för att eventuellt hitta linjer. 
% Börja från översta kanten och när en pixel hittas, se om det finns en
% följande linje. 
% https://se.mathworks.com/help/images/hough-transform.html
for i = 1:12
    I = rgb2gray(images{i});
    BW = edge(I,'canny', [0.4, 0.5]);
    %figure
    %imshow(BW);

    % Compute the Hough transform of the binary image returned by edge.
    [H,theta,rho] = hough(BW);

    % Find the peaks in the Hough transform matrix, H, using the houghpeaks function.
    P = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))));

    % Find lines in the image using the houghlines function.
    lines = houghlines(BW,theta,rho,P,'FillGap',5,'MinLength',7);

    % Calculate the angles for all lines compared to x-axis, and length of
    % them
    N = length(lines);
    angles = zeros(N,2);
    for k = 1:N
       a = lines(k).point2(1) - lines(k).point1(1);
       b = lines(k).point2(2) - lines(k).point1(2);
       c = sqrt(a^2 + b^2);

       angles(k,1) = rad2deg(acos(a/c)); % Angle from line to x-axis
       angles(k,2) = c; % Length of line
    end
    % Sort to only use the two longest lines
    sorted_angles = sortrows(angles, 2, 'descend');
    
    % Add to feature vector
    F(8,i) = 3*sorted_angles(1,1);
    F(9,i) = 3*sorted_angles(1,2);
    F(10,i) = 3*sorted_angles(2,1);
    F(11,i) = 3*sorted_angles(2,2);
    F(12,i) = 3*sorted_angles(3,1);
    F(13,i) = 3*sorted_angles(3,2);
    F(14,i) = 3*sorted_angles(4,1);
    F(15,i) = 3*sorted_angles(4,2);
end
%% Calculate distance between feature vectors
distances = zeros(12,12);
for j = 1:12
    for i = 1:12
        distances(j,i) = round(norm(F(:,j) - F(:,i)),1);
    end
end
