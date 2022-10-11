d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)

d.end()
