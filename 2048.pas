Program xax;
var 
 lebel : 2,3,4,5,6,7,8;
 i,j,m,c,d,e,f : integer;
 a : array [4..4] og integer;
 b : string;
begin
 i:=(1,4);.........................
 j:=(1,4);..........................
 a [i,j]:=2;
2 : m:=0;
 For j:= 1 to 4 do
  if a[i,j]>0 then m:=m+1;
 If m=16 then 
   for i:=1 to 4 do 
    for j:=1 to 3 do 
     if a[i,j]=a[i,j+1] then Goto 4;
   for i:=1 to 4 do 
    for j:=1 to 3 do 
     if a[j,i]=a[j+1,i] then Goto 4;
   write('Partutyun'); exit;
4 : while a[i,j]=0 do begin
     i:=(1,4)..............................
      j:=(1,4)..............................
    end;
 m:=(1,5);
 if m=5 then a[i,j]:=4
        else a[i,j]:=2:
 m:=0;
 For j:= 1 to 4 do
  if a[i,j]>0 then m:=m+1;
 If m=16 then 
   for i:=1 to 4 do 
    for j:=1 to 3 do 
     if a[i,j]=a[i,j+1] then Goto 1;
   for i:=1 to 4 do 
    for j:=1 to 3 do 
     if a[j,i]=a[j+1,i] then Goto 1;
   write('Partutyun'); exit;        
1 : For i:= 1 to 4 do begin writeln(' ');
  for j:= 1 to 4 do write (a[i,j],' ');
                   end;
 Writeln ('Yntreq uxxutyuny'); read(b);
 If ord (b[1])=R................... then begin
5: if i<4 then begin i:=i+1; c:=a[i,1]; d:=a[i,2]; e:=a[i,3]; f:=a[i,4]; Goto 3; end
          else Goto 1 end;
 If ord (b[1])=l................... then begin
6: if i<4 then begin i:=i+1; c:=a[i,4]; d:=a[i,3]; e:=a[i,2]; f:=a[i,1]; Goto 3; end
          else Goto 1 end;
 If ord (b[1])=d................... then begin
7: if i<4 then begin i:=i+1; c:=a[1,i]; d:=a[2,i]; e:=a[3,i]; f:=a[4,i]; Goto 3; end
          else Goto 1 end;
 If ord (b[1])=u................... then begin
8: if i<4 then begin i:=i+1; c:=a[4,i]; d:=a[3,i]; e:=a[2,i]; f:=a[1,i]; Goto 3; end
          else Goto 1 end
                                    else begin Writeln ('chka aydpisi uxxutyun'); Writeln ('Yntreq uxxutyuny'); read(b); Goto 5;
                                         end;
3: If f=0 then
           if e=0 then
                   if d=0 then begin 
                                f:=c;
                                c:=0;
                                Goto 2 ;
                               end
                          else 
                           if c=d then begin
                                        f:=2*c;
                                        c:=0;
                                        d:=0;
                                        Goto 2;
                                       end
                                  else begin
                                        f:=d;
                                        e:=c;
                                        d:=0;
                                        c:=0;
                                        Goto 2 ;
                                       end
                    else if d=0 then 
                                 if c=e then begin
                                              f:=2*e;
                                              e:=0;
                                              d:=0;
                                              c:=0;
                                              Goto 2;
                                             end
                                        else begin
                                              f:=e;
                                              e:=c;
                                              d:=0;
                                              c:=0;
                                              Goto 2;
                                             end
                                 else if d=e then begin
                                                   f:=2*e;
                                                   e:=c;
                                                   d:=0;
                                                   c:=0;
                                                  end
                                             else begin 
                                                   f:=e; 
                                                   if c=d then begin
                                                                e:=2*d;
                                                                d:=0;
                                                                c:=0;
                                                                Goto 2 ;
                                                               end
                                                          else begin
                                                                e:=d;
                                                                d:=c;
                                                                c:=0;
                                                                Goto 2 ;
                                                               end; end
           else if e=0 then 
                        if d=0 then 
                                if f=c then begin
                                             f:=2*f;
                                             c:=0;
                                             Goto 2;
                                            end
                                       else begin
                                             e:=c;
                                             c:=0;
                                             Goto 2;
                                            end
                               else if d=f then begin 
                                                 f:=2*f;
                                                 e:=c;
                                                 d:=0;
                                                 c:=0;
                                                 Goto 2 ;
                                                end
                                            else if c=d then begin
                                                              e:=2*d;
                                                              d:=0;
                                                              c:=0;
                                                              Goto 2 ;
                                                             end
                                                        else begin
                                                              e:=d;
                                                              d:=c;
                                                              c:=0;
                                                              Goto 2 ;
                                                             end
                        else if e=f then begin
                                          f:=2*f;
                                          if c=d then begin
                                                       e:=2*d;
                                                       d:=0;
                                                       c:=0;
                                                       Goto 2 ;
                                                      end
                                                 else begin
                                                       e:=d;
                                                       d:=c;
                                                       c:=0;
                                                       Goto2 ; 
                                                      end;
                                          end
                                    else if e=d then begin
                                                      e:=2*e;
                                                      d:=c;
                                                      c:=0;
                                                      Goto 2 ;
                                                     end
                                                else if d=0 then begin 
                                                                  d:=c;
                                                                  c:=0;
                                                                  Goto 2 ;
                                                                 end
                                                            else if d=c then begin
                                                                              d:=2*d;
                                                                              c:=0;
                                                                              Goto 2 ;
                                                                             end
                                                                        else Goto 2;
end.
                                                                        
                                                                              
                                                
                                                
                                     
                                              
                               
                                      
                                             
                                                                        
                                          
                                       
                   
                                   
  