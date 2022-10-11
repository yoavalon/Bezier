d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)

d.end()
