# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def getHostName(self,url):
        return url.split("//")[1].split("/")[0]
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostName=self.getHostName(startUrl)
        visited=set()
        def dfs(url,htmlParser):
            visited.add(url)
            for nextUrl in htmlParser.getUrls(url):
                if self.getHostName(nextUrl) == hostName and nextUrl not in visited:
                    #visited.add(nextUrl)
                    dfs(nextUrl,htmlParser)
        dfs(startUrl,htmlParser)
        
        return list(visited)