make_pos <- function(x) {
    x[x < 0] <- 0
    x
}

cut_thr <- function(x, p) {
    tmp <- quantile(y, probs = p)
    x[x < tmp] <- 0
    x
}

get_noise_level <- function(x, fs) {
    mean(stats::runmed(x, fs / 100))
}

moving_average <- function(x, n = 10) {
    stats::filter(x, rep(1/n, n), sides = 2)
}

squarify <- function(x) {
    x[x > 0] <- 1
    x
}

make_search_window <- function(x, fs) {
    ind_r <- which(diff(y) == 1) - fs/2
    ind_f <- which(diff(y) == -1) + fs/2
    list("r" = ind_r, "f"  = ind_f)
}

find_peak <- function(x, r, f) {
    N <- length(r)
    ind <- vector(mode = "numeric", length = N)
    amp <- vector(mode = "numeric", length = N)
    for (i in seq.int(N)) {
        amp[i] <- max(x[r[i]:f[i]])
        ind[i] <- r[i] + which.max(x[r[i]:f[i]])
    }
    list("amp" = amp, "ind" = ind)
}

library(neurone)
datafile <- PUT_DATA_HERE

## rec <- read.neurone(datafile, channels = c("VEOG", "HEOG"))
rec <- read.neurone(datafile)

## Plot a part of the data
t1          <- 1*60*500
t2          <- 3*60*500 + t1

fs          <- 500

x           <- rec$signal$VEOG$data[t1:t2]
x_m         <- stats::runmed(x, fs)

y           <- x - x_m
y           <- make_pos(y)
y           <- moving_average(y, fs/10)

y[is.na(y)] <- 0

y           <- cut_thr(y, p = 0.95)

y           <- squarify(y)

pla         <- make_search_window(y, fs)
pla2        <- find_peak(x, pla$r, pla$f)

plot(x, type = "l", col = "blue")
points(pla2$ind, pla2$amp, col = "red", pch = 1, cex = 3)
