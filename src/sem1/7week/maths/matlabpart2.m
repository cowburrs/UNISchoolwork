% We build the matrix P and you are required to use P to calculate the probability of winning by the
% end of turn n. Enter your solution in Ans below. Note that sol records the answer for different values of
% n and is then used to plot the graph

% Enter SL below
SL = [18 1; 20 2; 21 3; 22 4; 23 5; 24 6]

% Setting up P

% Construct P, ignorning the snakes and ladders
P = zeros(25);
for i=1:25
    for j=i+1:min(i+6,25)
        P(i,j) = 1/6;
    end
end
for i = 1:6
    P(25-6+i, 25) = min((i+1)/6, 1);
end

% Adjust for the snakes and ladders
no_SL=height(SL);
for i= 1:no_SL
    for j=1:25
        if j == SL(i,2)
            P(SL(i,1),j) = 1;
        else
            P(SL(i,1),j) = 0;
        end
    end
end

% Record the probability for different values of n
sol = [];
for n=1:10
    
    % Your value for the probability of winning by the end of turn n goes below
end
for n=1:15
    Rndm = P^n;
    Ans = Rndm(1, 25);;
    
    sol = [sol, Ans];
end

% Plot it out
stem(sol);
xlabel('n')
ylabel('probability')
