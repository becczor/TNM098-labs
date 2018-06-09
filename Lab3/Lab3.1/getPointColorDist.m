function [meanR, meanG, meanB] = getPointColorDist(image, x, y, d)
    square = image(x-d:x+d, y-d:y+d, :);
    
    %imshow(square)
    
    meanR = mean(mean(square(:,:,1)));
    meanG = mean(mean(square(:,:,2)));
    meanB = mean(mean(square(:,:,3)));


end