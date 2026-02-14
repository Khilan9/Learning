#include<bits/stdc++.h>
using namespace std;
int main(){
    // vector understanding
    vector<int> v={1,2};
    v.push_back(3);
    v.push_back(4);
    for(auto x:v)cout<<x;

    // set understanding
    set<int> st={1,2};
    st.insert(3);
    st.insert(4);
    cout<<bool(st.find(1)!=st.end());

    // stack understanding
    stack<int> stk;
    stk.push(1);
    stk.push(2);
    while(!stk.empty()){
        cout<<stk.top();
        stk.pop();
    }

    // queue understanding
    queue<int> q;
    q.push(1);
    q.push(2);
    while(!q.empty()){
        cout<<q.front();
        q.pop();
    }

    // priority queue understanding
    priority_queue<int> pq;
    pq.push(1);
    pq.push(3);
    pq.push(2);
    pq.top();
    while(!pq.empty()){
        cout<<pq.top();
        pq.pop();
    }

    // dequeue in c++ 
    deque<int> dq= {2, 3, 4};
    dq.push_front(1);
    dq.push_back(5);
    dq.pop_front();
    dq.pop_back();
    dq.at(2);
    dq.front();
    dq.back();


    // map
    unordered_map<int,int> ump;
    ump[1]=2;
    ump[2]=3;
    for(auto x:ump)cout<<x.first<<x.second;
    return 0;
}