d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
