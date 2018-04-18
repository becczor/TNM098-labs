function [centerX, centerY] = findCenterPoint(image)
    dims = size(image);
    centerX = ceil(dims(1) / 2);
    centerY = ceil(dims(2) / 2);
end