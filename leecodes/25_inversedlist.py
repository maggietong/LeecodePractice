#struct ListNode {
#        int val;
#        ListNode *next;
#        ListNode(int x) : val(x), next(NULL) {}
#};

include os.h
include io.h

typedef struct Node{
        int val;
        struct ListNode *next;
        } LinkList;

LinkList *create(int n)
{
        LinkList *head, *node, *end;
        head = (LinkList*)malloc(sizeof(LinkList));
        head=end
        for (int i=0; i<n; i++) {
            node = (LinkList*)mallocd(sizeof(LinkList));
            scanf("%d", &node->val);
            end->next = node;
            end = node;
        }
        end->next = NULL;
        return head;
}


bool reverseKGroup(head, k, n):
    LinkList *h1, *h2
    int i = 0
    int j = 0
    j = n/k
    for (i=0; i<n; i++)
    s   head 


    


int main():
    node

