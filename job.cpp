#include <iostream>
using namespace std;

void Scheduling(int profit[], int deadline[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (profit[j] > profit[i])
            {
                int temp = profit[j];
                profit[j] = profit[i];
                profit[i] = temp;

                int temp2 = deadline[j];
                deadline[j] = deadline[i];
                deadline[i] = temp2;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << profit[i] << " ";
    }
    cout<<endl;
    for (int i = 0; i < n; i++)
    {
        cout << deadline[i] <<" ";
    }
    cout<<endl;

    int jobSchedule[n]={-1};
    int cost = 0;
    int jobCount = 0;


    for (int i = 0; i < n; i++)
    {
        int j = deadline[i];
        if (j > 0 && jobSchedule[j - 1] == -1)
        {
            jobSchedule[j - 1] = i;
            cost += profit[i];
            jobCount += 1;
        }
        else
        {
            for (int k = j - 1; k >= 0; k--)
            {
                if (jobSchedule[k] == -1)
                {
                    jobSchedule[k] = i;
                    cost += profit[i];
                    jobCount += 1;
                    break;
                }
            }
        }
    }

    cout << "MAximum Profit: " << cost << endl;
    cout << "Jobs Selected: ";
    for (int i = 0; i < jobCount; i++)
    {
        cout << "J" << jobSchedule[i] + 1 << "->";
    }
}

int main()
{

    int n;
    // cout << "Enter no of jobs: ";
    // cin >> n;

    // int profit[n];
    // int deadline[n];

    // for (int i = 0; i < n; i++)
    // {
    //     cout << "Enter profit of " << i + 1 << "th job: ";
    //     cin >> profit[i];
    //     cout << "Enter deadline of " << i + 1 << "th job: ";
    //     cin >> deadline[i];
    // }
    int profit[7]={50,15,10,25};
    int deadlines[7]={2,1,2,1};

    Scheduling(profit, deadlines, 7);

    return 0;
}