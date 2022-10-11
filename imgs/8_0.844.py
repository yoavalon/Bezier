d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.position_pen(3,0)

d.end()
