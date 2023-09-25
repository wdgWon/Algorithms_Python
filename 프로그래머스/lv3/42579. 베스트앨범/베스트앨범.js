function solution(genres, plays) {
    const hash = {}
    const genreHash = {}
    
    for(let i = 0; i < genres.length; i++) {
        if(genres[i] in hash) {
            hash[genres[i]].push([plays[i],i]);
            hash[genres[i]].sort((a,b) => b[0] - a[0]);
            genreHash[genres[i]] += plays[i];
        }
        else {
            hash[genres[i]] = [[plays[i], i]];
            genreHash[genres[i]] = plays[i];
        }
    }
    
    const prior = Object.entries(genreHash).sort((a,b) => b[1] - a[1]);
    
    return prior.reduce((acc, cur) => [...acc, ...hash[cur[0]].slice(0,2).map(e => e[1])], [])
}