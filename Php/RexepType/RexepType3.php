<?php

namespace RexepType;

class RexepType3 extends RexepTypeAbstract
{
    private const PARSE = [
        '.*?PC:\s+([^\r\n]+)',
        '.*?User:\s+([^\r\n]+)',
        '.*?OS\sVersion:\s+([^\r\n]+)',
        '.*?Screen\sResoluton:\s+([^\r\n]+)',
        '.*?Language:\s+([^\r\n]+)',
        '.*?Physical\sInstalled\sMemory:\s+([^\r\n]+)',
        '.*?Country:\s+([^\r\n]+)',
    ];

    /**
     * @var string[]
     */
    private const PARAMS = [
        'computerName',
        'username',
        'operationSystem',
        'screenSize',
        'currentLanguage',
        'ram',
        'country',
        'zipCode',
        'location',
        'country',

    ];

    public static function parse(string $path)
    {
        $self = new self($path);
        return $self->generateParams(self::PARSE, self::PARAMS);
    }
}