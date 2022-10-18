d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)

d.end()
