(define (my-filter pred s)
  (if (null? s)
      nil
      (let ((rest (my-filter pred (cdr s))))
        (if (pred (car s))
            (cons (car s) rest)
            rest))))

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1)
     lst2)
    ((null? lst2)
     lst1)
    (else
     (append (list (car lst1) (car lst2))
             (interleave (cdr lst1) (cdr lst2))))))

(define (accumulate joiner start n term)
  (if (= n 0)
      start
      (joiner (accumulate joiner start (- n 1) term)
              (term n))))

(define (no-repeats lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (no-repeats
             (filter (lambda (x) (not (= x (car lst))))
                     (cdr lst))))))
