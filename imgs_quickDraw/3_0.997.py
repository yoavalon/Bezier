d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.position_pen(1,3)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)

d.end()
