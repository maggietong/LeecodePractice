#include <stdio.h> 
#include <string.h>

#define bool int
#define true 1
#define false 0

int isAnagram(char* s, char* t) 
{
    int n, m;
    n = strlen(s);
    m = strlen(t);
    if (n != m)
        return false;
    int a[26] = {0};
    int i = 0;
    for (i=0; i<n; i++) {
        a[s[i] - 'a']++;
        a[t[i] - 'a']--;
    }
    for (i=0; i<26; i++)
        if (a[i] != 0)
            return 0;
    return 1;

}

int main(void) {

    char *s = "abcde";
    char *t = "bcade";
    bool ret;

    ret = isAnagram(s, t);   
    printf("%i",ret);
    return 1;
}

