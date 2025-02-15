{

lookahead using peak map

(07) gol
(07) (adapted to Edison script) gol 

}


unit DSP_Lookahead;


interface


type TLookahead=class
          private
          FBufferLength,FTime,FBlockLength,FBlockShift,FBlockAnd,FBlockNotAnd:Integer;
          ValueBuffer,BlockBuffer:Array of Single;

          public

          constructor Create;
          destructor  Destroy; override;

          procedure   Reset;
          procedure   Input(Value:Single);
          function    GetPeak:Single;
          procedure   SetBufferLength(Value:Integer);
          procedure   SetBlockShift(Value:Integer);

          property Peak:Single read GetPeak;
          property BufferLength:Integer read FBufferLength write SetBufferLength;
          property BlockShift:Integer read FBlockShift write SetBlockShift;

        End;








implementation


// get the max volumes of a 32bit float mono wave buffer
type  PInteger=^Integer;

procedure GetAccurateWavePeak_32FM(SourceBuffer:PInteger;Length:Integer;var Vol:Single);
var   n,v:Integer;
Begin
v:=0;
for n:=0 to Length-1 do 
  Begin
  if SourceBuffer^>v then v:=SourceBuffer^;
  inc(Integer(SourceBuffer),4);
  End;
Vol:=Single(v);  
End;




constructor TLookahead.Create;
Begin
Inherited Create;

FBufferLength:=256;
BlockShift:=4;
End;


destructor TLookahead.Destroy;
Begin

Inherited Destroy;
End;




procedure TLookahead.Reset;
var   n:Integer;
Begin
for n:=0 to High(ValueBuffer) do ValueBuffer[n]:=0;
for n:=0 to High(BlockBuffer) do BlockBuffer[n]:=0;
FTime:=0;
End;


procedure TLookahead.SetBufferLength(Value:Integer);
Begin
if Value<1 then Value:=1;
FBufferLength:=Value;
SetLength(ValueBuffer,FBufferLength);
SetLength(BlockBuffer,(FBufferLength+FBlockAnd) shr FBlockShift);

Reset;
End;


procedure TLookahead.SetBlockShift(Value:Integer);
Begin
FBlockShift:=Value;
FBlockLength:=1 shl FBlockShift;
FBlockAnd:=FBlockLength-1;
FBlockNotAnd:=$FFFFFFFF xor FBlockAnd;

SetBufferLength(FBufferLength);
End;


procedure TLookahead.Input(Value:Single);
var   t:Integer;
Begin
// next
inc(FTime);
if FTime>=FBufferLength then FTime:=0;

// add to the circular buffer
ValueBuffer[FTime]:=Value;
t:=FTime shr FBlockShift;
if FTime and FBlockAnd=0 then BlockBuffer[t]:=Value
                         else
   if Value>BlockBuffer[t] then BlockBuffer[t]:=Value;
End;


function TLookahead.GetPeak:Single;
var   v:Single;
      t1,t2:Integer;
Begin
// first get peak of all blocks
GetAccurateWavePeak_32FM(@BlockBuffer[0],Length(BlockBuffer),Result);

// then get peak of remaining values in active block
t1:=FTime+1;
t2:=(FTime and FBlockNotAnd)+FBlockLength;
if t2>FBufferLength then t2:=FBufferLength;
if t2>t1 then 
   Begin
   GetAccurateWavePeak_32FM(@ValueBuffer[t1],t2-t1,v);
   if v>Result then Result:=v;
   End;
End;




end.




