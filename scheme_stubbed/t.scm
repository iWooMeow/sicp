(lambda (let int b) (+ let int b))

(let-to-lambda '(lambda
                 (let
                  a
                  b)
                 (+
                  let
                  a
                  b)))
