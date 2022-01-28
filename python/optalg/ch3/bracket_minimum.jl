# From algorithm 3.1

function bracket_minimum(f, x=0, s=1e-2, k=2.0)

    a, ya = x, f(x)
    b, yb = a + s, f(a + s)
    if yb > ya
        a, b = b, a
        ya, yb = yb, ya
        s = -s
    end
    while true
        c, yc = b + s, f(b + s)
        if yc > yb
            return (min(a,c), max(a,c))
        end
        a, ya, b, yb = b, yb, c, yc
        s *= k
    end
end


function test_f(x)
     return x^3 + 2 * x^2 + x + 3
end

@time a, b = bracket_minimum(test_f)
