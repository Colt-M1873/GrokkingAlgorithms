// https://leetcode.com/problems/copy-list-with-random-pointer/
// 2022 3.12
// To be finished
// iterative    √ 2022.03.12
// hashmap      √ 2022.03.12
// recursive    ×
// pyversion    ×


// Hashmap cpp https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1428603/2-Clean-C%2B%2B-SOLUTIONS-oror-HASHMAP-and-ONLY-POINTERS
// hashmap py https://leetcode.com/problems/copy-list-with-random-pointer/discuss/373694/Python3-Dictionary
// superfast https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)


# include <stdlib.h>
# include <unordered_map>

using namespace std;

//  Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};


class Solution {
public:
    Node* copyRandomList(Node* head) {
        // // v1 two pass, 
        // // the first loop create new listnode and copy all the val amd next, 
        // // the second loop fill all the random in the new listnode by 
        // // measureing the distance from every random pointed node to the end in the original listnode.
        // if(head==NULL){
        //     return NULL;
        // }
        // Node* oldP;
        // oldP=head;
        // Node* currNode=new Node(oldP->val);
        // Node* newp=currNode;
        // Node* retp=currNode;
        // int len=1;
        // while(oldP->next!=NULL){
        //     ++len;
        //     oldP=oldP->next;
        //     Node* currNode=new Node(oldP->val);
        //     newp->next=currNode;
        //     newp=newp->next;
        // }
        // newp=retp;
        // oldP=head;
        // Node* oldran;
        // while(oldP!=NULL){
        //     oldran=oldP->random;
        //     int d2end=0;
        //     while(oldran!=NULL){
        //         oldran=oldran->next;
        //         d2end++;
        //     }
        //     Node* newran=retp;
        //     int d2head=len-d2end;
        //     while (d2head!=0){
        //         d2head--;
        //         newran=newran->next;
        //         /* code */
        //     }
        //     newp->random=newran;            
        //     newp=newp->next;
        //     oldP=oldP->next;
        // }
        // return retp;
        // // v1 end

        // v2 copied hashmap
        // create a hashmap from each old node to new node
        // and use old node as the index to tacle the random part
        if(head==NULL) return NULL;
        unordered_map <Node*, Node*> umap;
        Node* curr=head;
        while(curr!=NULL){
            Node* currNode=new Node(curr->val);
            umap[curr]=currNode;
            curr=curr->next;
        }
        curr=head;
        while(curr!=NULL){
            umap[curr]->random=umap[curr->random];
            umap[curr]->next=umap[curr->next];
            curr=curr->next;
        }
        return umap[head];
        // v2 end
    }
};