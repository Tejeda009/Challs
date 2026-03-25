const data = atob('aXQwNG5kXzExbHM0X3ZuXzMzdmQzMXJzX190dGhuMzNfMXNsMGNse3VDdEUxUzBBblQhSX0=');
let secret = [];
let i = 0, j = data.length - 1, k = false;

while (j - i >= 0) {
    secret[k ? i : j] = data[j - i];
    if (k) { i++; k = false; } 
    else { j--; k = true; }
}
console.log(secret.join(''));