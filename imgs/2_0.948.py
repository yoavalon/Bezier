d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
