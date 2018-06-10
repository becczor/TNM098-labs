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
F = zeros(7,12);
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

%% Calculate distance between feature vectors

distances = zeros(1,12);
for i = 1:12
    distances(i) = norm(F(:,7) - F(:,i));
end


