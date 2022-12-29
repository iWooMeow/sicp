(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? asc-lst)
  (if (null? (cdr asc-lst))
      #t
      (and (<= (car asc-lst) (cadr asc-lst))
           (ascending? (cdr asc-lst)))))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= exp 1)   base)
    ((even? exp) (square (pow base (/ exp 2))))
    (else        (* base (pow base (- exp 1))))))

(define (even-subsets s)
  (if (null? s)
      nil
      (append (even-subsets (cdr s))
              (subset-helper even? s))))

(define (odd-subsets s)
  (if (null? s)
      nil
      (append (odd-subsets (cdr s))
              (subset-helper odd? s))))

(define (subset-helper f s)
  (append (map (lambda (x) (cons (car s) x))
               (if (f (car s))
                   (even-subsets (cdr s))
                   (odd-subsets (cdr s))))
          (if (f (car s))
              (list (list (car s)))
              nil)))

(define (non-empty-subsets s)
  (if (null? s)
      nil
      (append (list (list (car s)))
              (map (lambda (x) (cons (car s) x))
                   (non-empty-subsets (cdr s)))
              (non-empty-subsets (cdr s)))))

(define (even-filter-subsets s)
  (filter (lambda (x) (even? (apply + x)))
          (non-empty-subsets s)))
