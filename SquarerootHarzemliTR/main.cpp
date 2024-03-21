#include <iostream>
#include <iomanip>

using namespace std;

double karekokalma(double geldi)
{
    int i=0;

    while(i*i<=geldi)
        i++;

    --i;
    double yakinKok = i;
    double yakinKokKaresi = yakinKok*yakinKok;
    double sadeKok = geldi - yakinKokKaresi;
    double sonuc = (sadeKok / (yakinKok*2)) + yakinKok;

    return sonuc;
}

int main()
{
    double giris;

    cout << "giris: ";
    cin >> giris;

    cout << "sonuc: " << karekokalma(giris) << endl;

    return 0;
}
