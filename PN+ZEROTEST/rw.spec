vars
  X1 X2 X3 X4 X5 X6 X7

rules
	X1>=1 						-> X1'=X1-1, X2'=X2+1;
	X2>=1 						-> X2'=X2-1, X3'=X3+1;
	X2>=1 						-> X2'=X2-1, X4'=X4+1;
	X3>=1,X5>=1 					-> X3'=X3-1, X6'=X6+1;
	X4>=1,X5>=1,X6=0 				-> X4'=X4-1, X5'=X5-1, X7'=X7+1;
	X6>=1 						-> X6'=X6-1, X1'=X1+1;
	X7>=1 						-> X7'=X7-1, X5'=X5+1, X1'=X1+1;

init
	X1>=1,X2=0,X3=0,X4=0,X5=1,X6=0,X7=0
target 
	X6>=1,X7>=1
