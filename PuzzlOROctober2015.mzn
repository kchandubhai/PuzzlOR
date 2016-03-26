% PuzzlOR October 2015 Race car design

% let i represent race car part type
% let j represent part

% variables
var 0..5: x11;
var 0..5: x21;
var 0..5: x31;
var 0..5: x12;
var 0..5: x22;
var 0..5: x32;
var 0..5: x13;
var 0..5: x23;
var 0..5: x33;
var 0..5: x14;
var 0..5: x24;
var 0..5: x34;

% constraints
constraint <= 12;
constraint <= 17;
constraint <= 14;
constraint <= 13;
constraint <= 15;
constraint <= 11;
constraint <= 16;
constraint <= 19;
constraint <= 18;
constraint <= 20;


% objective function
solve minimize x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34;

% output
output ["fastest speed","\n",show(x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34)]
