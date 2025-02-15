{

parameter smoothing
(04) gol
(07) (adapted to Edison script) gol 

based on "Lowpass filter for parameter edge filtering" by Olli Niemitalo (http://www.musicdsp.org/showone.php?id=28)

}


unit DSP_Smoothing;


interface


const // smoothing types
      ST_Immediate=-1;
      ST_1Pole    =0;
      ST_3Pole    =1;


type  // smoothing memory
      TSmoothingMem=Record
          Mem:Array[0..2] of Double;
          InitValue:Double;
        End;

      // smoothing parameters
      TSmoothingParams=Record
          // public parameters
          SType:Integer;
          // coefficients
          Coef,Gain:Array[0..2] of Double;
        End;


const Smoothing_DefSmoothness=0.999;


procedure Smoothing_Init(var SmoothingParams:TSmoothingParams;SetType:Integer;SetScale,SetSmoothness:Double);
procedure Smoothing_Reset(var SmoothingMem:TSmoothingMem;SetValue:Double);
function  Smoothing_Process(var SmoothingParams:TSmoothingParams;var SmoothingMem:TSmoothingMem;Value:Double):Double;








implementation


function MaxOfD(a,b:Double):Double;
Begin
if a>b then Result:=a
       else Result:=b;
End;


// smoothing
procedure Smoothing_Init(var SmoothingParams:TSmoothingParams;SetType:Integer;SetScale,SetSmoothness:Double);
var   a,b,MasterGain:Double;
Begin
with SmoothingParams do
  Begin
  if SetScale<=0 then SetType:=ST_Immediate;
  SType:=SetType;

  Case SType of
       ST_1Pole:
         Begin
         // 1 pole
         Coef[0]:=Exp(Ln(0.01)/MaxOfD(SetScale,1));
         End;
       ST_3Pole:
         Begin
         // 3 pole
         a:=1-4.8/MaxOfD(SetScale,10);
         b:=SetSmoothness;
         Coef[0]:=a;
         Coef[1]:=a*b;
         Coef[2]:=a*b*b;

         MasterGain:=1/(-1/(Ln(a)+2*Ln(b))+2/(Ln(a)+Ln(b))-1.0/Ln(a));
         Gain[0]:=MasterGain;
         Gain[1]:=MasterGain*(Ln(a*b*b)*(Ln(a)-Ln(a*b))/((Ln(a*b*b)-Ln(a*b))*Ln(a*b))-Ln(a)/Ln(a*b));
         Gain[2]:=MasterGain*(-(Ln(a)-Ln(a*b))/(Ln(a*b*b)-Ln(a*b)));
         End;
    End;
  End;
End;


procedure Smoothing_Reset(var SmoothingMem:TSmoothingMem;SetValue:Double);
Begin
with SmoothingMem do
  Begin
  InitValue:=SetValue;
  Mem[0]:=0;
  Mem[1]:=0;
  Mem[2]:=0;
  End;
End;


function  Smoothing_Process(var SmoothingParams:TSmoothingParams;var SmoothingMem:TSmoothingMem;Value:Double):Double;
Begin
with SmoothingParams,SmoothingMem do
  Begin
  Case SType of
       ST_1Pole:
         Begin
         // 1 pole
         InitValue:=Value+(InitValue-Value)*Coef[0];
         Result:=InitValue;
         End;
       ST_3Pole:
         Begin
         // 3 pole
         Value:=Value-InitValue;

         Mem[0]:=Coef[0]*Mem[0]+Value;
         Mem[1]:=Coef[1]*Mem[1]+Value;
         Mem[2]:=Coef[2]*Mem[2]+Value;

         Result:=InitValue+Gain[0]*Mem[0]+Gain[1]*Mem[1]+Gain[2]*Mem[2];
         End;
       Else
         Begin
         // immediate
         Result:=Value;
         End;
    End;
  End;
End;








end.


