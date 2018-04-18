function [meanR, meanG, meanB] = meanColorImage(image)
    meanR = mean(mean(image(:,:,1)))
    meanB = mean(mean(image(:,:,2)))
    meanG = mean(mean(image(:,:,3)))
end