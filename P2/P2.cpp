#include <iostream>

using namespace std;
long long m_w, m_z;

int get_random() {
    m_z = 36969 * (m_z & 65535) + (m_z >> 16);
    m_w = 18000 * (m_w & 65535) + (m_w >> 16);
    long long res = (m_z << 16) + m_w;
    return res % 1000000000;
}
int partition(int arr[],int l,int r)
{
    int m=l;
    int pivot=l+rand()%(r-l+1);
    swap(arr[r],arr[pivot]);
    int x=arr[r];
    for(int i=l;i<r;i++)
    {
        if(arr[i]<x)
        {
            swap(arr[m],arr[i]);
            m++;
        }
    }
    swap(arr[m],arr[r]);
    return m;
}
int QuickSelect(int arr[], int l, int r, int k)
{
    if(r<l)
        return -1;

    int m=partition(arr,l,r);
    if(m==k)
        return arr[m];
    if(m>k)
        QuickSelect(arr,l,m-1,k);
    else QuickSelect(arr,m+1,r,k);
}
int kthSmallest(int arr[], int l, int r, int k)
{
    return QuickSelect(arr,l,r,k-1);
}

int main()
{
    int N, k;
    cin >> N >> k >> m_w >> m_z;
    int arr[N];
    for (int i = 0; i < N; ++i) {
        arr[i]= get_random();
    }
    cout << kthSmallest(arr, 0, N-1, k);
}

