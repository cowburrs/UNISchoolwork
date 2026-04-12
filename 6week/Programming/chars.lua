function dump(o)
	if type(o) == "table" then
		local keys = {}
		for k in pairs(o) do
			table.insert(keys, k)
		end
		table.sort(keys, function(a, b)
			if type(a) == type(b) then
				return a < b
			end
			return tostring(a) < tostring(b)
		end)
		local s = "{"
		for _, k in ipairs(keys) do
			local v = o[k]
			local fk = type(k) ~= "number" and '"' .. k .. '"' or k
			s = s .. "" .. fk .. " = " .. dump(v) .. ", "
		end
		return s .. "} "
	else
		return tonumber(o) and tostring(o) or '"' .. tostring(o) .. '"'
	end
end

-- local function summation(x)
-- 	if x <= 1 then
-- 		return 11
-- 	else
-- 		local m = x - 1
-- 		return summation(x - 1) + 17 * m ^ 2 + 22 * m
-- 	end
-- end
-- for i = 1, 5, 1 do
-- 	print(summation(i))
-- end
function summation(n)
	return 11 + 17 * (n - 1) * n * (2 * n - 1) / 6 + 22 * (n - 1) * n / 2
end
for i = 1, 5, 1 do
	print(summation(i))
end
local somestring = ""
for i = 0, 9, 1 do
    somestring = somestring .. " + 17*" .. i .. "^2"
    local n = i + 1
    local endcoefficient = ((n - 1) * n / 2)
    local printstring = "11 + 22*" .. endcoefficient .. somestring
    print(load("return " .. printstring)())
	 print(printstring)
end
