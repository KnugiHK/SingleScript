using Printf
function traverse(x)
    ceiling = trunc(Int, sqrt(x))
    for i in 3:2:ceiling
        if x % i == 0
            return false
        end
    end
    return true
end 

function is_prime(x)
    if x == 2
        return true
    else
        if x % 2 == 0
            return false
        else
            return traverse(x)
        end
    end
end


print(is_prime(parse(Int, ARGS[1])))
