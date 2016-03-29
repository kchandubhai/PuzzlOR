% PuzzlOR October 2015 Race car design

% let i represent race car part type { A - 1, B - 2, C - 3}
% let j represent part {engine - 1, tires - 2, trasmission - 3, brakes - 4}

% variables
var 0..10: x11;
var 0..10: x21;
var 0..10: x31;
var 0..10: x12;
var 0..10: x22;
var 0..10: x32;
var 0..10: x13;
var 0..10: x23;
var 0..10: x33;
var 0..10: x14;
var 0..10: x24;
var 0..10: x34;

% constraints
constraint x11 + x12 + x13 + x34 <= 12;
constraint x31 + x22 + x13 + x34 <= 17;
constraint x31 + x12 + x23 + x24 <= 14;
constraint x21 + x22 + x13 + x34 <= 13;
constraint x11 + x22 + x23 + x14 <= 15;
constraint x11 + x32 + x23 + x34 <= 11;
constraint x21 + x32 + x33 + x14 <= 16;
constraint x21 + x22 + x13 + x24 <= 19;
constraint x31 + x12 + x33 + x14 <= 18;
constraint x31 + x32 + x33 + x24 <= 20;
 constraint x11 + x21 + x31 >= 1;
 constraint x12 + x22 + x32 >= 1;
 constraint x13 + x23 + x33 >= 1;
 constraint x14 + x24 + x34 >= 1;
constraint x11 + x21 + x31 + x12 + x22 + x32 + x13 + x23 + x33 + x14 + x24 + x34 <= 4;


% objective function
solve minimize x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34;

% output
output ["fastest speed ",show(x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34),"\n",
"awes engine ",show(x11),"\n",
"Baller engine ", show(x21),"\n",
"harm engine ",show(x31),"\n",
"Aero tires ", show(x12),"\n",
"awes tires ",show(x22),"\n",
"Baller tires ", show(x32),"\n",
"awes transmission ",show(x13),"\n",
"Baller transmission ", show(x23),"\n",
"awes transmission ",show(x33),"\n",
"Baller brakes ", show(x14),"\n",
"awes brakes ",show(x24),"\n",
"Baller brakes ", show(x34),"\n"
]
