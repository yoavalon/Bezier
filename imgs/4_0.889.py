d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)

d.end()
