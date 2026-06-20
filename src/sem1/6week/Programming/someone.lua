local function summation(x)
	if x <= 1 then
		return 11
	else
		local m = x - 1
		return summation(x - 1) + 17 * m ^ 2 + 22
	end
end
for i = 1, 5, 1 do
	print(summation(i))
end
function summation(n)
	return 11 + 17 * (n - 1) * n * (2 * n - 1) / 6 + 22 * (n - 1)
end
for i = 1, 5, 1 do
	print(summation(i))
end
local somestring = ""
for i = 0, 4, 1 do
	somestring = somestring .. " + 17*" .. i .. "^2"
	local endcoefficient = i
	local printstring = "11 + 22*" .. endcoefficient .. somestring
	print(load("return " .. printstring)())
	-- print(printstring)
end
