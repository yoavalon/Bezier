d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,0)

d.end()
