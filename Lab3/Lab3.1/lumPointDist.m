function [lum] = lumPointDist(image, x, y, d)
    square = image(x-d:x+d, y-d:y+d, :);
    figure;
    subplot(1,2,1);
    imshow(square)
    
    squareLab = rgb2lab(square);
    lumArea = squareLab(:,:,1);
    
    subplot(1,2,2)
    imshow(lumArea,[0 100]);
    
    lum = mean2(lumArea);
    
end