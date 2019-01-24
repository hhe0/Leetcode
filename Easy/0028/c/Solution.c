int strStr(char* haystack, char* needle) {
    int s_len = strlen(haystack);
	int t_len = strlen(needle);
	int i;
	int j;
	int temp;

	if (0 == t_len)
	{
		return 0;
	}

	for (i = 0; i < s_len; i++)
	{
		temp = i;
		for (j = 0; j < t_len; j++)
		{
			if (haystack[temp++] != needle[j])
			{
				break;
			}
		}
		if (j == t_len)
		{
			return i;
		}
	}

	return -1;
}