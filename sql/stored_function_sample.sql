
-- 副問い合わせをストアドプロシージャの呼び出しに置き換えるサンプル
-- [before] SELECT * FROM SALES_RESULTS WHERE AMOUNT >= SELECT AVG(AMOUNT) FROM SALES_RESULTS;
-- [after ] SELECT * FROM SALES_RESULTS WHERE AMOUNT >= AVERAGE_AMOUNT();

-- サンプル用のテーブル (売り上げ実績)
CREATE TABLE SALES_RESULTS(
    NAME VARCHAR(10), -- 会社名
    DATE DATE, -- 取引日
    AMOUNT INT -- 売上高
);

-- サンプルデータ
INSERT INTO SALES_RESULTS VALUES
('A', '2019/03/31', 100),
('B', '2019/04/01', 200),
('C', '2019/04/02', 300);

-- ストアドファンクションの利用を有効にする
SET GLOBAL log_bin_trust_function_creators=1;

-- SALES_RESULTS.AMOUNT の平均値を取得するストアドファンクションを定義する
delimiter //
CREATE FUNCTION AVERAGE_AMOUNT() RETURNS DOUBLE
BEGIN
DECLARE R DOUBLE;
SELECT AVG(AMOUNT) INTO R FROM SALES_RESULTS;
RETURN R;
END
//
delimiter ;

-- AMOUNT が平均以上のレコードを取得する
-- 実際は修正前の状態でも大して複雑ではないので、実務だったら下記のような修正は必要ないと思う

-- 修正前 (WHERE句に副問い合わせがある)
-- SELECT * FROM SALES_RESULTS WHERE AMOUNT >= SELECT AVG(AMOUNT) FROM SALES_RESULTS;

-- 修正後 (副問い合わせの部分をストアドファンクションとして外に出す)
SELECT * FROM SALES_RESULTS WHERE AMOUNT >= AVERAGE_AMOUNT();
