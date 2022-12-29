(define (over-or-under num1 num2)
  ; (cond 
  ; ((< num1 num2) -1)
  ; ((= num1 num2) 0)
  ; (else          1)))
  (if (< num1 num2)
      -1
      (if (= num1 num2)
          0
          1)))

(define (make-adder num) (lambda (x) (+ x num)))

(define (composed f g)
  (define (helper x) (f (g x)))
  helper)

(define lst ; '((1) 2 (3 4) 5)
        (cons (list 1) (cons 2 (list (list 3 4) 5))))

(define (duplicate lst)
  (if (null? lst)
      nil
      (append (list (car lst) (car lst))
              (duplicate (cdr lst)))))
