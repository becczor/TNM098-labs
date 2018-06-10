%% Använd binärfilerna och gå igenom dem för att eventuellt hitta linjer. 
% Börja från översta kanten och när en pixel hittas, se om det finns en
% följande linje. 
% https://se.mathworks.com/help/images/hough-transform.html
I = rgb2gray(images{5});
BW = edge(I,'canny', [0.4, 0.5]);
figure
imshow(BW);

%% Compute the Hough transform of the binary image returned by edge.
[H,theta,rho] = hough(BW);

%% Display the transform, H, returned by the hough function.
figure
imshow(imadjust(rescale(H)),[],...
       'XData',theta,...
       'YData',rho,...
       'InitialMagnification','fit');
xlabel('\theta (degrees)')
ylabel('\rho')
axis on
axis normal 
hold on
colormap(gca,hot)

%% Find the peaks in the Hough transform matrix, H, using the houghpeaks function.
P = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))));

%% Superimpose a plot on the image of the transform that identifies the peaks.

x = theta(P(:,2));
y = rho(P(:,1));
plot(x,y,'s','color','black');

%% Find lines in the image using the houghlines function.
lines = houghlines(BW,theta,rho,P,'FillGap',5,'MinLength',7);

%% Create a plot that displays the original image with the lines superimposed on it.

figure, imshow(I), hold on
max_len = 0;
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');

   % Determine the endpoints of the longest line segment
   len = norm(lines(k).point1 - lines(k).point2);
   if ( len > max_len)
      max_len = len;
      xy_long = xy;
   end
end
% highlight the longest line segment
plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','red');


%% Calculate the angles for all lines compared to x-axis
N = length(lines);
angles = zeros(N,2);
for k = 1:N
   a = lines(k).point2(1) - lines(k).point1(1);
   b = lines(k).point2(2) - lines(k).point1(2);
   c = sqrt(a^2 + b^2);
   
   angles(k,1) = rad2deg(acos(a/c));
   angles(k,2) = c; 
   
end

sorted_angles = sortrows(angles, 2, 'descend');