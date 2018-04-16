%im = imread('01.jpg', 'jpg');
%imshow(im(:,:,1))

rgbImage = imread('01.jpg', 'jpg');

if rgbImage(1, 1, :) == rgbImage(2, 2, :)
    disp("hej")
end
