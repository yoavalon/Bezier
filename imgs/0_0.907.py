d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)

d.end()
