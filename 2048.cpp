#include <iostream>
#include <math.h>
#include <cstdlib>
using namespace std;

void step(int &x, int &y, int &z, int &q, int &e)
 {
   if (q == 0)
    if (z == 0)
     if (y == 0)
      { q = x; x = 0; if (q != 0) e = 1; }
     else
     if (y == x)
      { q = 2 * x; x = 0; y = 0; e = 1; }
     else
      { q = y; z = x; x = 0; y = 0; e = 1; }
    else
    if (y == 0)
     if (x == z)
      { q = 2 * x; x = 0; z = 0; e = 1; }
     else
      { q = z; z = x; x = 0; e = 1; }
    else
     if (y == z)
      { q = 2 * y; z = x; y = 0; x = 0; e = 1; }
     else
     if (x == y)
      { q = z; z = 2 * x; y = 0; x = 0; e = 1;}
     else
      { q = z; z = y; y = x; x = 0; e = 1;}
   else
   if (z == 0)
    if (y == 0)
     if (x == q)
      { q = 2 * x; x = 0; e = 1;}
     else {
      if (x != 0)
       { z = x; x = 0; e = 1; } }
    else
    if (q == y)
     { q = 2 * y; z = x; y = 0; x = 0; e = 1; }
    else
    if (y == x)
     { z = 2 * y; y = 0; x = 0; e = 1; }
    else
     { z = y; y = x; x = 0; e = 1; }
   else
   if (y == 0)
    if (q == z)
     { q = 2 * z; z = x; x = 0; e = 1; }
    else
    if (z == x)
     { z = 2 * x; x = 0; e = 1; }
    else {
     if (x != 0)
      { y = x; x = 0; e = 1; } }
   else
   if (q == z)
    if (y == x)
     { q = 2 * z; z = 2 * x; y = 0; x = 0; e = 1; }
    else
     { q = 2 * z; z = y; y = x ; x = 0; e = 1; }
   else
    if (z == y)
     { z = 2 * y; y = x; x = 0; e = 1; }
    else
     if (y == x)
      { y = 2 * x; x = 0; e = 1; }
 }

int main()
{
 int a[5][5],b[5][5],c[17],i,j,k,l,p,st,possibility,game;
 char s,last[5];

 cout<<"Hello!"<<endl;
 cout<<"This is game 2048"<<endl;
 game = 1;
 while(game == 1)
{
 l = rand() % 6 +1;
 for (i=1;i<5;i++)
  for (j=1;j<5;j++)
   a[i][j] = 0;

 for(k=1;k<17;k++) c[k] = 0;
 k = 1;
 for(i=1;i<5;i++)
  for(j=1;j<5;j++)
   if(a[i][j] == 0)
    { c[k] = 10 * i + j; k++; }
 if (k != 1) {
  k--;
  k = rand() % k +1;
  if (l == 6)
   l = 4;
  else
   l = 2;
  i = c[k] / 10;
  j = c[k] % 10;
  a[i][j] = l; }
  //input 2/4

 cout<<endl<<" ";
 for(i=1;i<8;i++) cout<<"_";
 cout<<endl;
 for(i=1;i<5;i++) {
  for(j=1;j<5;j++)
   cout<<"|"<<a[i][j];
  cout<<"|"<<endl;
  for(j=1;j<10;j++)
   cout<<"-";
  cout<<endl; }
 cout<<" ";
 cout<<endl;
  //input a[][]
 for (i=1;i<5;i++)
  for (j=1;j<5;j++)
   b[i][j] = a[i][j];

 cout<<"Please press"<<endl;
 cout<<" w - for up"<<endl;
 cout<<" s - for down"<<endl;
 cout<<" a - for left"<<endl;
 cout<<" d - for right"<<endl;
 cout<<"  u - for go back 1 step"<<endl;
 cout<<endl<<" r - for restart"<<endl;
 cout<<"And f - for finish game"<<endl;
 cout<<"=============================="<<endl;
 possibility = 1;
 st = 1;        //the last step is worked
 last[1] = 'l'; //==u if you can undo
 last[3] = 'l'; //==w if you can't w or s
 last[2] = 'l'; //==a if you can't a or d
 last[4] = 'l'; //==u if program must do undo or you will lose
 while(possibility == 1 and game == 1)
{
  st = 0;
  if (last[4] == 'u') s = 'u';
  else
  cin>>s; //what step is
  p = 1;
  if (last[3] == 'w')
    if (s == 'w' or s == 's')
     p = 0;
  else
    if (last[2] == 'a')
     if (s == 'a' or s == 'd')
      p = 0;
  if (p == 1)
    if (s == 'w' or s == 's' or s == 'a' or s == 'd')
     {
      for (i=1;i<5;i++)
       for (j=1;j<5;j++)
        b[i][j] = a[i][j];
     }
  if (p == 1)
  if (s == 'w')
   for(i=1;i<5;i++)
    step(a[4][i],a[3][i],a[2][i],a[1][i],st);
  else
  if (s == 's')
   for(i=1;i<5;i++)
    step(a[1][i],a[2][i],a[3][i],a[4][i],st);
  else
  if (s == 'a')
   for(i=1;i<5;i++)
    step(a[i][4],a[i][3],a[i][2],a[i][1],st);
  else
  if (s == 'd')
   for(i=1;i<5;i++)
    step(a[i][1],a[i][2],a[i][3],a[i][4],st);
  else
  if (s == 'f') game = 0;
  else
  if (s == 'r') possibility = 0;
  else
  if (s == 'u')
   if (last[1] == 'u') {
    for (i=1;i<5;i++)
     for (j=1;j<5;j++)
      a[i][j] = b[i][j];
    last[1] = 'l'; last[2] = 'l'; last[3] = 'l'; last[4] = 'l';
    cout<<endl<<" ";
    for(i=1;i<8;i++) cout<<"_";
     cout<<endl;
    for(i=1;i<5;i++) {
     for(j=1;j<5;j++)
      cout<<"|"<<a[i][j];
     cout<<"|"<<endl;
     for(j=1;j<10;j++)
      cout<<"-";
     cout<<endl; }
    cout<<" ";
    cout<<endl;
     //input a[][]
                      }
   else
    { cout<<"Sorry,you can't do undo"<<endl;
    cout<<"Please,select another step"<<endl; }
    //step

 if (st == 1)
{
 last[1] = 'u';
 for(k=1;k<17;k++) c[k] = 0;
 k = 1;
 for(i=1;i<5;i++)
  for(j=1;j<5;j++)
   if(a[i][j] == 0)
    { c[k] = 10 * i + j; k++; }
 if (k != 1) {
  k--;
  k = rand() % k +1;
  l = rand() % 6 +1;
  if (l == 6)
   l = 4;
  else
   l = 2;
  i = c[k] / 10;
  j = c[k] % 10;
  a[i][j] = l; }
   //input 2/4

 cout<<endl<<" ";
 for(i=1;i<8;i++) cout<<"_";
  cout<<endl;
 for(i=1;i<5;i++) {
  for(j=1;j<5;j++)
   cout<<"|"<<a[i][j];
  cout<<"|"<<endl;
  for(j=1;j<10;j++)
   cout<<"-";
  cout<<endl; }
 cout<<" ";
 cout<<endl;
  //input a[][]

 possibility = 2;
 for(i=1;i<5;i++)
  for(j=1;j<4;j++)
   if (a[i][j] == 0 or a[i][j+1] == 0 or a[i][j] == a[i][j+1])
    possibility = 1;
 if (possibility == 2)
  last[2] = 'a';
 possibility = 2;
 for(i=1;i<5;i++)
  for(j=1;j<4;j++)
   if (a[j][i] == 0 or a[j+1][i] == 0 or a[j][i] == a[j+1][i])
    possibility = 1;
 if (possibility == 2)
    last[3] = 'w';
 possibility = 1;
 if (last[2] == 'a' and last[3] == 'w')
 {
  cout<<"Please press"<<endl;
  cout<<" u - for undo"<<endl;
  cout<<" or f - for finish"<<endl;
  cout<<"And any key - for restart"<<endl;
  cin>>s;
 }
}
if (st == 1 ) {
 if (last[2] == 'a' and last[3] == 'w')
  if (s == 'f') game = 0;
  else
  if (s == 'u') {last[4] = 'u';last[2] = 'l';last[3] = 'l';}
  else
   possibility = 0;
 else
  last[1] == 'u';
              }
else
 if (s == 'w' or s == 's' or s == 'a' or s == 'd')
 {
    cout<<"Your step is invalid"<<endl;
    cout<<"Please,select another step"<<endl; }
 else
 if (s != 'r' and s != 'f' and s != 'u')
   { cout<<"Your step does not exist"<<endl;
    cout<<"Please,select a right step"<<endl; }
}
}
}
