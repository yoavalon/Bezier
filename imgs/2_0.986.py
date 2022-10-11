d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)

d.end()
