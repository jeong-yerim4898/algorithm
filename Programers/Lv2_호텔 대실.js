const changeNumber = (str) => {
    const [h,m] = str.split(":");
    return +h * 60 + +m;
}

function solution(book_time) {
    const time = book_time.map(time=>[changeNumber(time[0]),changeNumber(time[1])+10]);
    time.sort((a,b)=>a[0]-b[0]);
    let ret = 0;
    let room = [];

    for (const [start,end] of time) {
        room = room.filter(r=>r[1]>start);
        room.push([start,end]);
        ret = ret > room.length?ret:room.length
    }
    return ret
}