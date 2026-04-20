local function rndm(str, x, y, neg)
	if x > y / 2 then
		return str
	end
	local onenum
	local twonum
	onenum = y + 1 - x
	twonum = x
	if neg < 0 then
		twonum = onenum
		onenum = x
	end
	return rndm(str .. onenum .. " " .. twonum .. "; ", x + 2, y, -neg)
end
print(rndm("", 2, 25, 1))
