d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,0)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)

d.end()
