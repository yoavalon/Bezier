d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)

d.end()
