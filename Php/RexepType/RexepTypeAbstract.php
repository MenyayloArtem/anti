<?php

namespace RexepType;

abstract class RexepTypeAbstract
{
    protected string $path;
    private array $result = [];

    protected function generateParams(array $regularExpression, $params): array
    {
//        // Кринж
//        $logPath = __DIR__;
//        $logPath = explode("\\", $logPath);
//        array_pop($logPath);
//        array_pop($logPath);
//        $logPath = join("\\", $logPath);
//        $logPath .= "\logs\\";

        $match = array_map(function (string $rx) {
            preg_match('/' . $rx . '/s', (string) file_get_contents("logs/" . $this->path), $match);
            [1 => $param] = $match;
            return $param;
        }, $regularExpression);

        $this->setParam($match, $params);

        return $this->result;
    }

    private function setParam($match, $params): void
    {
        for ($i = 1; $i <= count($params); $i++) {
            if ($params[$i-1] === 'ram' && (static::class === RexepType1::class || static::class === RexepType2::class)) {
                $match[$i] = round((int)$match[$i] / (1024 ** 3));
            }
            elseif ($params[$i-1] === 'ram' && static::class === RexepType3::class){
                $match[$i] = round((int)$match[$i] / 1024);
            }
            $this->result[$params[$i-1]] =  $match[$i] ?? null;
        }
    }

    abstract static function parse(string $path);
}