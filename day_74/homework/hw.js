function rounding(n, m) {
    idk = Math.round(n / m)*m;
    if (idk / 2 === n){
        return n;
    }
    return idk
}
i