#include <bits/stdc++.h>

struct SegTree{

    unsigned long long size;
    std::vector<long long> sums;

    void init(int n){
        size = 1;
        while(size < n) size *= 2;
        sums.assign(2 * size, 0ll);
    }

    long long sum(size_t x, size_t xi, size_t yi, size_t xj, size_t yj) {
        if (yj < xi || xj >= yi){ // Completely outside
            return 0;
        }

        if (xi <= xj && yj <= yi){ // Completely inside
            return sums[x];
        }

        size_t m = (xj + yj) / 2;

        if (yi < m){
            return sum(2 * x + 1, xi, yi, xj, m);
        } else if (xi >= m){
            return sum(2 * x + 2, xi, yi, m, yj);
        } else {
            return sum(2 * x + 1, xi, yi, xj, m) + sum(2 * x + 2, xi, yi, m, yj);
        }
    }

    long long sum(size_t sx, size_t sy){
        return sum(0, sx, sy, 0, size);
    }

    void set(long long val, size_t i, size_t x, size_t lx, size_t rx){
        /*
        lx, ly : boundaries of segment
        i : target index of the element to place
        x : recursive index
        val : the actual value
        */
        if (rx - lx == 1){ // We found the place
            sums[x] = val;
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            set(val, i, 2 * x + 1, lx, m);
        } else {
            set(val, i, 2 * x + 2, m, rx);
        }

        sums[x] = sums[2 * x + 1] + sums[2 * x + 2];
    }

    void set(long long val, size_t i){
        set(val, i, 0, 0, size);
    }

};

int main() {

    int n, m;
    std::cin >> n >> m;

    std::vector<int> values (n);

    SegTree st = SegTree();
    st.init(n);

    for (int i = 0; i < n; i++){
        std::cin >> values[i];
        st.set(values[i], i);
    }

    while (m--){
        long long op, a, b;
        std::cin >> op >> a >> b;
        if (op == 1){
            st.set(b, a);
        } else {
            std::cout << st.sum(a, b) << std::endl;
        }
    }

    return 0;
}