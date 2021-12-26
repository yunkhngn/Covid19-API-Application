
#include <stdio.h>
#include <conio.h>
void Vecaythong(int h)
{
// vẽ thân cây
for (int i = 1; i <= h; i++)
{
//in khoảng trắng ra
for (int j = 1; j <= h - i; j++)
{
printf(" ");
}
//in * để làm cây
for (int k = 1; k <= i; k++)
{
printf("* ");
}
printf("\n");
}
// vẽ gốc cây
for (int i = 1; i <= 3; i++)
{
for (int j = 1; j < h - 2; j++)
{
printf(" ");
}
for (int k = 1; k <= 3; k++)
{
printf("**");
}
printf("\n");
}
}
int main()
{
Vecaythong(20);
_getch();
return 1;
}