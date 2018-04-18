function [meanColor] = meanColorChannel(channel)
    meanColor = mean(mean(channel));
end